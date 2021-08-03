import { Component, OnInit } from '@angular/core';

import { QuizService } from '../services/quiz.service';

import { Option, Question, Quiz, QuizConfig } from '../models/index';


@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css'],
  providers: [QuizService]
})
export class QuizComponent implements OnInit {
  quizes: any[];
  quiz: Quiz = new Quiz(null);
  mode = 'quiz';
  quizName: string;
  config: QuizConfig = {
    'allowBack': true,
    'allowReview': true,
    'autoMove': false,  // if true, it will move to next question automatically when answered.
    'duration': 300,  // indicates the time (in secs) in which quiz needs to be completed. 0 means unlimited.
    'pageSize': 1,
    'requiredAll': false,  // indicates if you must answer all the questions before submitting.
    'richText': false,
    'shuffleQuestions': false,
    'shuffleOptions': false,
    'showClock': false,
    'showPager': true,
    'theme': 'none'
  };

  pager = {
    index: 0,
    size: 1,
    count: 1
  };
  timer: any = null;
  startTime: Date;
  endTime: Date;
  ellapsedTime = '00:00';
  duration = '';
  total_answered: number = 0;
  submitted: boolean = false;
  report: boolean = false;
  answers: any[];

  // charts content
  title: string;
  piechart_data1: (string | number)[][];
  piechart_data2: (string | number)[][];
  piechart_data3: (string | number)[][];
  type: string;
  options: {};
  height: number;
  width: number;
  report_data: (string | number)[][];
  report_options: { colors : string[], isStacked : boolean };

  constructor(private quizService: QuizService) { }

  ngOnInit() {
    this.quizes = this.quizService.getAll();
    this.quizName = this.quizes[0].id;
    this.loadQuiz(this.quizName);
  }

  loadQuiz(quizName: string) {
    this.quizService.get(quizName).subscribe(res => {
      this.quiz = new Quiz(res);
      this.pager.count = this.quiz.questions.length;
      this.startTime = new Date();
      this.ellapsedTime = '00:00';
      this.timer = setInterval(() => { this.tick(); }, 1000);
      this.duration = this.parseTime(this.config.duration);
    });
    this.mode = 'quiz';
  }

  tick() {
    const now = new Date();
    const diff = (now.getTime() - this.startTime.getTime()) / 1000;
    if (diff >= this.config.duration && this.submitted == false) {
      this.onSubmit();
    }
    this.ellapsedTime = this.parseTime(diff);
  }

  parseTime(totalSeconds: number) {
    let mins: string | number = Math.floor(totalSeconds / 60);
    let secs: string | number = Math.round(totalSeconds % 60);
    mins = (mins < 10 ? '0' : '') + mins;
    secs = (secs < 10 ? '0' : '') + secs;
    return `${mins}:${secs}`;
  }

  get filteredQuestions() {
    return (this.quiz.questions) ?
      this.quiz.questions.slice(this.pager.index, this.pager.index + this.pager.size) : [];
  }

  onSelect(question: Question, option: Option) {
    if (question.questionTypeId === 1) {
      question.options.forEach((x) => { if (x.id !== option.id) x.selected = false; });
    }

    if (this.config.autoMove) {
      this.goTo(this.pager.index + 1);
    }
  }

  goTo(index: number) {
    if (index >= 0 && index < this.pager.count) {
      this.pager.index = index;
      this.mode = 'quiz';
    }
  }

  isAnswered(question: Question) {
    return question.options.find(x => x.selected) ? 'Answered' : 'Not Answered';
  };

  isCorrect(question: Question) {
    // let list_results = [];
     return question.options.every(x => x.selected === x.isAnswer) ? ('correct') : 'wrong';
  };

  onSubmit() {
    this.submitted = true;
    this.answers = [];
    this.quiz.questions.forEach(x => this.answers.push({ 'quizId': this.quiz.id, 'questionId': x.id, 'answered': this.isCorrect(x), "type": x.questionType.name}));

    // Post your data to the server here. answers contains the questionId and the users' answer.
    console.log(this.quiz);
    console.log(this.answers);
    this.answers.forEach(x => x.answered == 'correct' ? this.total_answered += 1 : this.total_answered);
    console.log(this.total_answered);
    this.display_analysis();
  }

  display_analysis()
  {
      
      let types_chapters = {"arithmetic": {"total":0, "correct":0}, "algebra": {"total":0, "correct":0}, "geometry": {"total":0, "correct":0}};  // type : [tot, correct_ans]
      for(let i=0; i< 5; i++)
      {
        // console.log(this.answers[i]["type"], types_chapters[this.answers[i]["type"]]["total"]);
          if(this.answers[i]["answered"] == "correct")
              types_chapters[this.answers[i]["type"]] ["correct"] += 1;
          types_chapters[this.answers[i]["type"] ]["total"] += 1;
      }
      console.log(types_chapters);

      // this.title = 'googlechart';  
      this.type = 'PieChart';  
      this.piechart_data1 = [  
     ['Correct', types_chapters["arithmetic"]["correct"]],  
     ['Incorrect', types_chapters["arithmetic"]["total"] - types_chapters["arithmetic"]["correct"]],   
  ];  
      this.piechart_data2 = [
        ['Correct', types_chapters["geometry"]["correct"]],
        ['Incorrect', types_chapters["geometry"]["total"] - types_chapters["geometry"]["correct"]]
      ];
      // this.columnNames = ['Correct', ''];  
      this.options = {   
        colors : ["#728dc4", "#3366cc"] ,
          pieHole: 0.4,  
      };  
      this.width = 500;  
      this.height = 300;  

      this.report_data = [
        [ "Maths", this.total_answered, 5 - this.total_answered]
      ];
      this.report_options = {
        colors : ["#e8832b", "#eaa970"],
        isStacked: true
      };
      this.mode = 'result';
  }
}
