import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { QuestionSet, ListChapters } from './interface';

@Injectable({
  providedIn: 'root'
})
export class AppserviceService {
  headers: HttpHeaders;

  constructor(private http: HttpClient) { }

  base_url = "http://127.0.0.1:5000/";
  // @app.route('/practice/maths/<chapterName>/<num_quest>')

  get_practice_questions(subject_name, chapter_name, num_questions) : Observable<QuestionSet[]>
  {
    let url = this.base_url + "practice/"+subject_name+"/"+chapter_name+"/"+num_questions;
    return this.http.get<QuestionSet[]>(url);
  }

  get_list_chapters(subject_name) : Observable<ListChapters>
  {
    let url = this.base_url + "practice/"+ subject_name;
    return this.http.get<ListChapters>(url);
  }

  // login_user(uid, pwd) : Observable<UserData>
  // {
  //   let url = this.base_url + 'login';
  //   this.headers = new HttpHeaders();
  //   return this.http.post<UserData>(url, {userid:uid, password: pwd}, { headers: this.headers} );
  // }
}
