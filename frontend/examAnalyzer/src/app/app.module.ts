import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { LearnComponent } from './learn/learn.component';
import { FormsModule } from '@angular/forms';
import * as $ from 'jquery';
import { SubjectComponent } from './learn/subject/subject.component';
import { PracticeComponent } from './practice/practice.component';
import { AppserviceService } from './appservice.service';
import { HttpClientModule} from '@angular/common/http';

import { QuizComponent } from './QuizComponent/quiz/quiz.component';
import { GoogleChartsModule } from 'angular-google-charts';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    LearnComponent,
    SubjectComponent,
    PracticeComponent,
    QuizComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    GoogleChartsModule
  ],
  providers: [ AppserviceService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
