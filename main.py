if __name__ == "__main__":
  # Introduction to Python Set comprehension

  tags = {  "Django", "Pandas", "Numpy" }
  print(tags)

  lower_tags = set()
  for tag in tags:
    lower_tags.add(tag.lower())
  print(lower_tags)

  lower_tags = set(map(lambda tag: tag.lower() , tags))
  print(lower_tags)

  lower_tags = { tag.lower() for tag in tags }
  print(lower_tags)

  new_tags = { tag.lower() for tag in tags if tag != "Numpy" }
  print(new_tags)
