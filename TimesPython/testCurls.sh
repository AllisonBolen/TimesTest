# should return info from the document
curl -X GET http://127.0.0.1:5000/document

# should say: You added the answer: YES to question This is super cool, right?.
# will add question answer section to the document
curl -i -H "Content-Type: application/json" -X POST -d '{"A":"YES", "Q":"This is super cool, right?"}' http://localhost:5000/document

# should say: You edited question 2 to: How is your cat?
# will edit the question or answer, depending on what tag is included, given a section number value in the document
curl -i -H "Content-Type: application/json" -X PATCH -d '{"Q":"How is your cat?", "num":"2"}' http://localhost:5000/document
# should say: You edited the answer: SURE to question 2.%
curl -i -H "Content-Type: application/json" -X PATCH -d '{"A":"SURE", "num":"2"}' http://localhost:5000/document

# should say: You edited the answer and question for section : 2.
# will edit a section of information in the document depending on the number given
curl -i -H "Content-Type: application/json" -X PUT -d '{"A":"NO", "Q":"Do you like olives?", "num":"2"}' http://localhost:5000/document

# should say: You deleted Question: 2
# will delete a question/answer or a question answer pair from the document depending on the secition number and tags provided
curl -i -H "Content-Type: application/json" -X DELETE -d '{"Q":"", "num":"2"}' http://localhost:5000/document
# should say: You deleted Answer: 2
curl -i -H "Content-Type: application/json" -X DELETE -d '{"A":"", "num":"2"}' http://localhost:5000/document
#should say: You deleted section: 2
curl -i -H "Content-Type: application/json" -X DELETE -d '{"A":"", "Q":"", "num":"2"}' http://localhost:5000/document
