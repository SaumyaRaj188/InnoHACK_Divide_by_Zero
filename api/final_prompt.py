
def translate(client,trans_lang,trans_type,content,auth_key=0):
    
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a text/website translation model"},
      {"role": "user", "content": '''
I will give you the content to translate, the to and from languages, the writing style, method of translation.
Style can be formal,informal,humourous,etc or auto(preserve the nuance).
Do not translate links or functions.
Do not translate language selection menu
You are not supposed to call any links.
Return only the translation.''' },
      {"role": "assistant", "content": "Sure! Provide me text"},
      {"role": "user", "content": f"trans_lang:{trans_lang}\ntrans_style:{trans_type}\ncontent:{content}"}
    ]
  )

  if (auth_key!=0):
    pass
  else:
    pass
  return completion.choices[0].message.content

if __name__=="__main__":
  from openai import OpenAI
  client = OpenAI(api_key='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')
  print(translate(client,trans_lang="Hindi",trans_type="auto",content='''hello how are you'''))