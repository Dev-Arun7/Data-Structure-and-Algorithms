
// Iterate over the documents using the forEach method
db.school.find().forEach(function(document) {
    printjson(document);
});
