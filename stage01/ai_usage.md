# SmartCare AI Usage

## AI Tool Used

Microsoft CoPilot

## Purpose of AI Use

I used AI as a tutor to help me understand the SmartCare Python code, identify possible limitations, and suggest improvements to the prototype created.

## Prompt Used

Act as a Python tutor.

I am learning introductory software technology.

Here is a small appointment-booking function.

1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

## AI Suggestions

The AI identified the following limitations:

1. The program only validates the patient name and does not fully validate the other appointment information.
2. The program does not check whether the same practitioner has two appointments at the same time.
3. The appointment time is not validated.

The AI suggested adding input validation and considering how conflicting appointments should be handled.

## How I Evaluated the AI Response

I did not accept each suggestion that AI recommended to me. I compared the suggestions with the SmartCare requirements and considered whether each suggestion was useful, clear, correct and what was required for the prototype.

## How I Verified the AI Output

I checked the AI suggestions by reviewing and running the Python code. I tested normal and unusual inputs, as well as a normal appointment, a blank patient name, two appointments with the same practitioner and time, and a 'none' appointment time.

This showed me which problems actually occurred and determine which AI suggestions were appropriate to use in the final product and which were not.
