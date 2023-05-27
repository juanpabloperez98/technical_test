import { Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { AuthGuard } from './guards/auth.guard';
import { ShowDataComponent } from './show-data/show-data.component';

export const Approutes: Routes = [
  {
    path: '',
    component: LoginComponent,
    pathMatch: 'full'

  },
  {
    path: 'registrarse',
    component: RegisterComponent,
    pathMatch: 'full'

  },
  {
    path: 'show_data',
    component: ShowDataComponent,
    canActivate:[AuthGuard],
    pathMatch: 'full'

  },
  {
    path: '**',
    redirectTo: ''
  }
]
