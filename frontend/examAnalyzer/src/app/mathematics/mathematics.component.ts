import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-mathematics',
  templateUrl: './mathematics.component.html',
  styleUrls: ['./mathematics.component.css']
})
export class MathematicsComponent implements OnInit {

  maths
  constructor() { }

  ngOnInit(): void {
  this.maths= [
    {
      id: 1,
      title: 'SETS',
      view: 'https://www.youtube.com/watch?v=p4kYez5IFQw',
      imgUrl: 'assets/z1.png',
      
    },

    {
      id: 2,
      title: 'RELATIONS AND FUNCTIONS',
      view: 'https://www.youtube.com/watch?v=8p4yXdUGRuE',
      imgUrl: 'assets/z26.png',
      
    },


    {
      id: 3,
      title: 'TRIGNOMETRIC FUNCTIONS',
      view: 'https://www.youtube.com/watch?v=cMqetVG8vRU',
      imgUrl: 'assets/z27.png',
       
    },

    {
      id: 4,
      title: 'COMPLEX NUMBERS AND QUADRATIC EQUATIONS',
      view: 'https://www.youtube.com/watch?v=Ov84TelHAkY',
      imgUrl: 'assets/z21.png',
     
    },

    {
      id: 5,
      title: 'PERMUTATIONS AND COMBINATIONS',
      view: 'https://www.youtube.com/watch?v=GmMX3-nTWbE',
      imgUrl: 'assets/z4.png',
       
    },



    {
      id: 6,
      title: 'SEQUENCES AND SERIES',
      view: 'https://www.youtube.com/watch?v=XJnIdRXUi7A',
      imgUrl: 'assets/z21.png',
    },



    {
      id: 7,
      title: 'STRAIGHT LINES',
      view: 'https://www.youtube.com/watch?v=VgVJrSJxkDk',
      imgUrl: 'assets/z2.png',
      
    },



    {
      id: 8,
      title: 'CONIC SECTION',
      view: 'https://www.youtube.com/watch?v=uOboYVGdwVg',
      imgUrl: 'assets/z9.png', 
    },


    {
      id: 9,
      title: 'MATHEMATICAL REASONING',
      view: 'https://www.youtube.com/watch?v=0A7RR0oy2ho',
      imgUrl: 'assets/z28.png',
       
    },


    {
      id: 10,
      title:  'STATISTICS',
      view: 'https://www.youtube.com/watch?v=OV-_g6rYvrk',
      imgUrl: 'assets/z27.png',
      
    },


    {
      id: 11,
      title: 'PROBABILITY',
      view: 'https://personal-portfolio0320.000webhostapp.com/',
      imgUrl: 'assets/z12.png',
      
    },


    {
      id: 12,
      title: 'DIFFERENTITAION',
      view: 'https://www.youtube.com/watch?v=lZSL7Tm5ViA',
      imgUrl: 'assets/z14.png',
      
    },

    {
      id: 13,
      title: 'INTEGRATION',
      view: 'https://www.youtube.com/watch?v=9AI3BkKQhn0',
      imgUrl: 'assets/z13.png',
     
    },

    {
      id: 14,
      title: 'LINEAR INEQUALITIES',
      view: 'https://www.youtube.com/watch?v=g-Aym5nJheM',
      imgUrl: 'assets/z14.png',
     
    },
  ]
}
}


