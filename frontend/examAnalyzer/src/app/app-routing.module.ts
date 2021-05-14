import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {HomeComponent} from './home/home.component';
import { LearnComponent } from './learn/learn.component';

const routes: Routes = [
  {path : '',pathMatch:'full',component:LoginComponent},
  {path: 'home', pathMatch:'full', component:HomeComponent,},
  {path:'learn', pathMatch:'full', component:LearnComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
