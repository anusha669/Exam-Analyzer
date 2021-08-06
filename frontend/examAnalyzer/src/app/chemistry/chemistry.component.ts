import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chemistry',
  templateUrl: './chemistry.component.html',
  styleUrls: ['./chemistry.component.css']
})
export class ChemistryComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
chemistry=[
{
  id: 1,
  title: 'SOLID STATE',
  view: 'https://www.youtube.com/watch?v=CMwGopvmGo8',
  imgUrl: 'assets/solid.png',
  
},

{
  id: 2,
  title: 'SOLUTIONS',
  view: 'https://www.youtube.com/watch?v=8p4yXdUGRuE',
  imgUrl: 'assets/sol.png',
  
},


{
  id: 3,
  title: 'REDOX REACTIONS',
  view: 'https://www.youtube.com/watch?v=cMqetVG8vRU',
  imgUrl: 'assets/rex.png',
   
},

{
  id: 4,
  title: 'HYDROGEN',
  view: 'https://www.youtube.com/watch?v=Ov84TelHAkY',
  imgUrl: 'assets/hyd.png',
 
},


{
  id: 5,
  title: 'F BLOCK ELEMENTS',
  view: 'https://www.youtube.com/watch?v=GmMX3-nTWbE',
  imgUrl: 'assets/fblock.png',
   
},



{
  id: 6,
  title: 'SURFACE CHEMISTRY',
  view: 'https://www.youtube.com/watch?v=XJnIdRXUi7A',
  imgUrl: 'assets/sol.png',
},



{
  id: 7,
  title: 'S BLOCK ELEMENTS',
  view: 'https://www.youtube.com/watch?v=VgVJrSJxkDk',
  imgUrl: 'assets/sblock.png',
  
},



{
  id: 8,
  title: 'POLYMERS',
  view: 'https://www.youtube.com/watch?v=uOboYVGdwVg',
  imgUrl: 'assets/poly.png', 
},


{
  id: 9,
  title: 'BIOMOLECULES',
  view: 'https://www.youtube.com/watch?v=0A7RR0oy2ho',
  imgUrl: 'assets/bio.png',
   
},


{
  id: 10,
  title:  'HALOALKANES',
  view: 'https://www.youtube.com/watch?v=OV-_g6rYvrk',
  imgUrl: 'assets/halo.png',
  
},


{
  id: 11,
  title: 'CHEMICAL KINETICS',
  view: 'https://personal-portfolio0320.000webhostapp.com/',
  imgUrl: 'assets/chem.png',
  
},


{
  id: 12,
  title: 'P BLOCK ELEMENTS',
  view: 'https://www.youtube.com/watch?v=lZSL7Tm5ViA',
  imgUrl: 'assets/pblock.png',
  
},

{
  id: 13,
  title: 'THERMODYNAMICS',
  view: 'https://www.youtube.com/watch?v=9AI3BkKQhn0',
  imgUrl: 'assets/therm.png',
 
},

{
  id: 14,
  title: 'KINETICS',
  view: 'https://www.youtube.com/watch?v=g-Aym5nJheM',
  imgUrl: 'assets/kine.png',
 
},
]
}