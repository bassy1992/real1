
import { GoogleGenAI, Type } from "@google/genai";
import { Property } from "../types";

const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

export async function analyzePropertyQuery(query: string, properties: Property[]) {
  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: `
      Act as a luxury real estate consultant for Bellrock Holdings. 
      The user is asking: "${query}"
      
      Here is our current inventory:
      ${JSON.stringify(properties.map(p => ({ id: p.id, title: p.title, location: p.location, price: p.price, beds: p.beds })))}
      
      Suggest the best properties (provide IDs) from our inventory and explain why they fit the user's needs in a sophisticated, professional tone. 
      Limit your response to a JSON array of suggestions.
    `,
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.OBJECT,
        properties: {
          suggestions: {
            type: Type.ARRAY,
            items: {
              type: Type.OBJECT,
              properties: {
                propertyId: { type: Type.STRING },
                reasoning: { type: Type.STRING }
              },
              required: ["propertyId", "reasoning"]
            }
          },
          generalAdvice: { type: Type.STRING }
        },
        required: ["suggestions", "generalAdvice"]
      }
    }
  });

  return JSON.parse(response.text);
}

export async function generatePropertyDescription(property: Property) {
  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: `Write a poetic and high-end marketing description for this property: ${JSON.stringify(property)}. Focus on the lifestyle and exclusivity of Bellrock Holdings.`,
  });
  return response.text;
}
