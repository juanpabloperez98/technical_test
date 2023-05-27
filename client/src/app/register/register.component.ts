import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, ValidationErrors } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  registerForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router,
  ) {
    this.registerForm = this.fb.group({
      name: ['', [Validators.required]],
      username: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
    });
  }

  ngOnInit(): void {
  }

  onSubmit() {

    const body = {
      'name': this.registerForm.get('name')!.value,
      'username': this.registerForm.get('username')!.value,
      'email': this.registerForm.get('email')!.value,
      'password': this.registerForm.get('password')!.value
    }

    this.authService.createUserService('register', body)
      .subscribe((res: string) => {
        this.router.navigate(['/'])
        Swal.fire('Proceso exitoso', 'Su usuario se ha creado correctamente', 'success');
      },(err: any) => {
        console.log(err);
      })
  }

}
