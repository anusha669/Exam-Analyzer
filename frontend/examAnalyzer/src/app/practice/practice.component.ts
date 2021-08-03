import { Component, OnInit } from '@angular/core';
import { AppserviceService } from '../appservice.service';

@Component({
  selector: 'app-practice',
  templateUrl: './practice.component.html',
  styleUrls: ['./practice.component.css']
})
export class PracticeComponent implements OnInit {
  practice_questions: any[];
  chapter_name_maths = ["Conic Section", "Statistics"];
  chapter_name_physics = ["Gravity", "thermodevices"];
  chapter_name_chemistry = ["oxides"];
  display_practice_questions: boolean;
  num_questions = 3;
  index_question: number = 0;
  current_question_display: any;
  shownDiv: boolean = false;
  subject_choosen: string = '' ;
  chapter_choosen: string;
  num_choosen: number = 5;
  list_chapter_name: any;
  correctly_answered: string;

  constructor(private serv: AppserviceService) { }

  ngOnInit(): void {
    // this.get_practice_questions('maths','Conic Section', '1');
  }

  get_practice_questions(subject_name, chapter_name, num_questions)
  {
    this.serv.get_practice_questions(subject_name, chapter_name, num_questions).subscribe(data => 
      {
        this.practice_questions = data["result"];
        this.display_practice_questions = true;
        console.log(this.practice_questions);
        this.current_practice_question(0);
      });
  }

  display_answer(option_choosen)
  {
    if(option_choosen == this.current_question_display.questionSet.answer[0])
    {
      this.correctly_answered = 'green';
    }
    else
    {
      console.log("false");
      this.correctly_answered = 'red';
    }
    this.shownDiv = ! this.shownDiv;
    // this.current_practice_question(1);
  }
  current_practice_question(num)
  {
    this.shownDiv = false;
    this.index_question = (this.index_question + num) % this.num_questions;
    this.current_question_display = this.practice_questions[this.index_question];
    console.log(this.current_question_display);
  }

  get_list_chapters()
  {
    this.serv.get_list_chapters(this.subject_choosen).subscribe(
      data => {
        this.list_chapter_name = data['chapters'];
        console.log(this.list_chapter_name);
      }
    ); 
  }



}
