import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppserviceService } from 'src/app/appservice.service';

@Injectable()
export class QuizService {

  constructor(private http: HttpClient, private serv: AppserviceService) { }

  get(url: string) {
    return this.http.get(url);
  }

  getAll() {
    return [
      { id: 'data/phy.json', name: 'Physics' },
      { id: 'assets/maths.json', name: 'Maths' },
      { id: 'data/chemi.json', name: 'Chemistry' }
    ];
  }

  get_expected_marks(quizName, marks_obtained){
      let data = this.serv.user_data["test_scores"]["maths"];
      return this.http.get("http://127.0.0.1:5000/expected_marks/"+ this.serv.user_data["userid"] +"/maths/"+marks_obtained+"/"+data);
  }
}
