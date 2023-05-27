import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { AuthService } from './auth.service';


@Injectable({
  providedIn: 'root'
})
export class ProcesoService {

  private url = environment.url_api;
  private securityHeaders = new HttpHeaders({
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': `Bearer ${ this.authservice.getToken() }`
  });

  constructor(
    private httpClient: HttpClient,
    private authservice: AuthService
  ) { }

  getProcesos( endPoint: string, type_: string, _id: string ){
    const url = `${this.url}/${endPoint}/${type_}/${_id}`;
    return this.httpClient.get(url, {headers: this.securityHeaders});
  }
}
