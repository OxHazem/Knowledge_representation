# **Mini Project 2**

# **Project Description**

You are developing a program that converts English sentences into predicate logic expressions and vice versa. The program will support quantifiers and allow users to input statements in both English and predicate logic notation.

# **Tasks:**

1. ## **English Sentences to Predicate Conversion:**

Implement a function that converts English sentences into predicate logic expressions.

Support quantifiers like "all," "some," "no," etc., and map them to ∀x, ∃x, ¬∀x, ¬∃x, etc., respectively.

2. ## **Predicate to English Sentences Conversion:**

Implement a function that converts predicate logic expressions into English sentences.

Support quantifiers like ∀x, ∃x, ¬∀x, ¬∃x, etc., and map them to "all," "some," "no," etc., respectively.

# **Example Conversion Tasks:**

1. English to Predicate Conversion: Input: "All dinosaurs are extinct."

Output: "∀x (is\_dinosaur(x) → is\_extinct(x))" 2- Predicate to English Conversion:

Input: "∃x (is\_animal(x) ∧ is\_endangered(x))" Output: "Some animals are endangered."

# **Hint:**

1. Use these words to express quantifiers (**All, every, each, no, none, some, a, an.)**

2. Use only these predicates (**are: →, is: →, are not: →, is not: →)**

3. You can use logical connectors like and, OR

**Note: Show at least one example of testing the validity of both functions.**