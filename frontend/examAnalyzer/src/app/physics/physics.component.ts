import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-physics',
  templateUrl: './physics.component.html',
  styleUrls: ['./physics.component.css']
})
export class PhysicsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  Physics= [
    {
      id: 1,
      title: 'WAVE',
      view: 'https://www.youtube.com/watch?v=KWzyQKcJBYg',
      imgUrl: 'assets/wave.png',
      
    },

    {
      id: 2,
      title: 'FORCE',
      view: 'https://www.youtube.com/watch?v=8p4yXdUGRuE',
      imgUrl: 'assets/Force.png',
      
    },


    {
      id: 3,
      title: 'OSCILLATIONS',
      view: 'https://www.youtube.com/watch?v=cMqetVG8vRU',
      imgUrl: 'assets/oscilation.png',
       
    },

    {
      id: 4,
      title: 'GRAVITATION',
      view: 'https://www.youtube.com/watch?v=Ov84TelHAkY',
      imgUrl: 'assets/gravitation.png',
     
    },


    {
      id: 5,
      title: 'MOTION IN STRAIGHT LINE',
      view: 'https://www.youtube.com/watch?v=GmMX3-nTWbE',
      imgUrl: 'assets/motion.png',
       
    },



    {
      id: 6,
      title: 'THERMODYNAMICS',
      view: 'https://www.youtube.com/watch?v=XJnIdRXUi7A',
      imgUrl: 'assets/thermo.png',
    },



    {
      id: 7,
      title: 'KINETIC THEORY',
      view: 'https://www.youtube.com/watch?v=VgVJrSJxkDk',
      imgUrl: 'assets/kinetics.png',
      
    },



    {
      id: 8,
      title: 'UNIT AND MEASUREMENTS',
      view: 'https://www.youtube.com/watch?v=uOboYVGdwVg',
      imgUrl: 'assets/unit.png', 
    },


    {
      id: 9,
      title: 'PHYSICAL WORLD',
      view: 'https://www.youtube.com/watch?v=0A7RR0oy2ho',
      imgUrl: 'assets/phy.png',
       
    },


    {
      id: 10,
      title:  'MECHANICAL PROPERTIES OF FLUIDS',
      view: 'https://www.youtube.com/watch?v=OV-_g6rYvrk',
      imgUrl: 'assets/Force.png',
      
    },


    {
      id: 11,
      title: 'ATOMS',
      view: 'https://personal-portfolio0320.000webhostapp.com/',
      imgUrl: 'assets/atom.png',
      
    },


    {
      id: 12,
      title: 'NUCLEI',
      view: 'https://www.youtube.com/watch?v=lZSL7Tm5ViA',
      imgUrl: 'assets/nuclei.png',
      
    },

    {
      id: 13,
      title: 'COMMUNICATION SYSTEMS',
      view: 'https://www.youtube.com/watch?v=9AI3BkKQhn0',
      imgUrl: 'assets/communi.png',
     
    },

    {
      id: 14,
      title: 'ELECTROMAGNETIC WAVES',
      view: 'https://www.youtube.com/watch?v=g-Aym5nJheM',
      imgUrl: 'assets/emwave.png',
     
    },
  ]
}
