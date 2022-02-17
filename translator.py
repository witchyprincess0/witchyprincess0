english_word = input('type your english word:')

translator = {
  "merry":"god",
  "christmas":"jul",
  "and":"och",
  "happy":"gott",
  "new":"nytt",
  'year':"ar"
}
swedish_word = (translator.get(english_word))

if swedish_word:
  print(f'The swedish word for {english_word} is {swedish_word}')
else:
  print (f'The swedish word for {english_word} does not exist.')
