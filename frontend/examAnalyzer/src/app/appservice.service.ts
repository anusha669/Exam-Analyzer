import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { QuestionSet, ListChapters, UserData } from './interface';
import { Router, ActivatedRoute } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AppserviceService {
  headers: HttpHeaders;
  user_data: UserData;

  constructor(private http: HttpClient, private route: Router) { }

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

  login_user(data)
  {
    let url = this.base_url + 'login/'+data["user_id"]+'/'+data["user_password"];
    this.headers = new HttpHeaders();
    this.http.get(url).subscribe(data => {
      this.user_data = data["result"][0];
      console.log(this.user_data);
      if(this.user_data.class == 1 || this.user_data.class == 2)
          this.route.navigate(['/learn']);
      
    });
  }
}
