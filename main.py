from openai import OpenAI
client = OpenAI()

word = "beer"
n_words = 15
n_sentences = 10
sentences = []

for i in range(n_sentences):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Complete a short sentence, wwith approximately {n_words} words long."},
            {"role": "user", "content": f"The {word}"}
        ],
        response_format={"type": "text"},
        temperature=1.6,
        max_completion_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        store=True
    )
    sentences.append(completion.choices[0].message.content)

for sentence in sentences:
    print(sentence)