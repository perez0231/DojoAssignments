var mongoose = require('mongoose');

var QuestionSchema = new mongoose.Schema({
  question: { type: String, required: [true, "question required"], minlength:[5, "pass mst be 10"] },
  description: String,
  answers: [{type: mongoose.Schema.Types.ObjectId, ref: 'Answer'}],
  }, {timestamps: true})

var Question = mongoose.model('Question', QuestionSchema);
