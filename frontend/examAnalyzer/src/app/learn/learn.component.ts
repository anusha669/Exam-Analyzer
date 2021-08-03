import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-learn',
  templateUrl: './learn.component.html',
  styleUrls: ['./learn.component.css']
})
export class LearnComponent implements OnInit {
  display_home: boolean = true;
  display_progress: boolean = false;
  display_completed: boolean = false;
  display_lessons: boolean = false;

  constructor( public activatedRoute: ActivatedRoute, private router: Router ) { }
  ngOnInit(): void {
  }

  home_display(){
    this.display_home = true;
    this.display_progress = false;
    this.display_completed = false;
    console.log("Within h, c",this.display_home,this.display_completed);
  }
  progress_display(){
    this.display_progress = true;
    this.display_home = false;
    this.display_completed = false;
  }
  completed_display(){
    this.display_completed = true;
    this.display_home = false;
    this.display_progress = false;
    console.log("Within h, c",this.display_home,this.display_completed);
  }
  subject_lessons(subject_name){
    console.log(subject_name,"op");
    this.display_lessons = true;
  }
}
