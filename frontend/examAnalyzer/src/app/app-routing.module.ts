import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {HomeComponent} from './home/home.component';
import { LearnComponent } from './learn/learn.component';
import { SubjectComponent } from './learn/subject/subject.component';
import { PracticeComponent } from './practice/practice.component';
import { QuizComponent } from './QuizComponent/quiz/quiz.component';
import { MathematicsComponent } from './mathematics/mathematics.component';
import { ChemistryComponent } from './chemistry/chemistry.component';

const routes: Routes = [
  {path : '',pathMatch:'full',component:LoginComponent},
  {path: 'home', pathMatch:'full', component:HomeComponent,},
  {path:'learn', component:LearnComponent,
    children: [
      {path:'subject', component:SubjectComponent}
    ]
  },
  {path:'practice', pathMatch:'full', component:PracticeComponent},
  {path:'exam', pathMatch:'full', component:QuizComponent},
  {path:'learn/mathematics', pathMatch:'full', component:MathematicsComponent},
  {path:'learn/chemistry', pathMatch:'full', component: ChemistryComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
