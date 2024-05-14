import pandas as pd

df = pd.read_csv("clues.csv")
print(df[['clue', 'answer']].head(10))

def is_valid_entry(row):
     return isinstance(row['clue'], str) and isinstance(row['answer'], str) and row['clue'] and row['answer']


# valid_count = 0
# invalid_count = 0

# for index, row in df.iterrows():
#     if is_valid_entry(row):
#          valid_count += 1
#     else:
#            invalid_count += 1



#rmove all null clue/answers
filtered_df = df[df['clue'].notna() & df['answer'].notna()]

print(len(df))
print("filtered : ", len(filtered_df))


#transform data into T5 compatible instruction: answer: format
finetuning_data = []
for i in range(len(filtered_df)):
  clue = df.loc[i, "clue"]
  answer = df.loc[i, "answer"]
  finetuning_data.append({
      'instruction': f"Solve the following crossword clue: {clue}",
      'answer': answer
  })

# Create a new DataFrame for CSV export
output_df = pd.DataFrame(finetuning_data)

# Save the output to a CSV file
output_df.to_csv("t5_finetuning_data.csv", index=False) 
