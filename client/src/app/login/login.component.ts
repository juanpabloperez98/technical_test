import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, ValidationErrors } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  ioauthtoken:string = "";
  loginForm!: FormGroup;

  constructor(
    private authService: AuthService,
    private fb: FormBuilder,
    private router: Router,
  ) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
    })
   }

  ngOnInit(): void {
  }

  onLoginSubmit() {

    if (this.loginForm.valid) {
      const body = {
        'email': this.loginForm.get('email')!.value,
        'password': this.loginForm.get('password')!.value,
      }
      this.authService.loginService(`login`, body)
        .subscribe( (res:any) => {
          this.ioauthtoken = res.token;
          this.authService.setToken(this.ioauthtoken);
          this.router.navigate(['/show_data']);
        }, (err: any) => {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: err.error.msg
          });
        })
    }
  }

}
