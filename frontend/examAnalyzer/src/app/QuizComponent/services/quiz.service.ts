import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable()
export class QuizService {

  constructor(private http: HttpClient) { }

  get(url: string) {
    return this.http.get(url);
  }

  getAll() {
    return [
      { id: 'data/phy.json', name: 'Physics' },
      { id: 'data/maths.json', name: 'Maths' },
      { id: 'data/chemi.json', name: 'Chemistry' }
    ];
  }

}
