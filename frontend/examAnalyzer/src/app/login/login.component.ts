import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { AppserviceService } from '../appservice.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user_id = "";
  user_password = "";
  display_validation: boolean = false;
  user_data: any;

  constructor( public activatedRoute: ActivatedRoute, private router: Router, private serv: AppserviceService  ) { }
  ngOnInit(){
      $(document).ready(function(){
          $('.login-info-box').fadeOut();
          $('.login-show').addClass('show-log-panel');
      });
      
      
      $('.login-reg-panel input[type="radio"]').on('change', function() {
          if($('#log-login-show').is(':checked')) {
              $('.register-info-box').fadeOut(); 
              $('.login-info-box').fadeIn();
              
              $('.white-panel').addClass('right-log');
              $('.register-show').addClass('show-log-panel');
              $('.login-show').removeClass('show-log-panel');
              
          }
          else if($('#log-reg-show').is(':checked')) {
              $('.register-info-box').fadeIn();
              $('.login-info-box').fadeOut();
              
              $('.white-panel').removeClass('right-log');
              
              $('.login-show').addClass('show-log-panel');
              $('.register-show').removeClass('show-log-panel');
          }
      });
    }

  login_user(credentials){
    console.log(this.user_id, this.user_password + "not displayed");
    console.log(credentials);
    if(this.user_id == "" || this.user_password == "")
        this.display_validation = true;
    else
    {  // this.router.navigate(['items'], { relativeTo: this.activatedRoute });
      // this.router.navigate(['/learn']);
        let data = this.serv.login_user(credentials);
            if(data["result"].length != 0){
                this.display_validation = false;
                this.router.navigate(['/learn']);
            }
            else
                this.display_validation = true;
    }
  }
}

