import { Component, OnInit } from '@angular/core';
import { ProcesoService } from '../proceso.service';
import { FormGroup, FormBuilder, Validators, ValidationErrors } from '@angular/forms';
import Swal from 'sweetalert2';


@Component({
  selector: 'app-show-data',
  templateUrl: './show-data.component.html',
  styleUrls: ['./show-data.component.css']
})
export class ShowDataComponent implements OnInit {

  data: any[] = [];

  dataSearchForm!: FormGroup;

  constructor(
    private procesoService: ProcesoService,
    private fb: FormBuilder,
  ) {
    this.dataSearchForm = this.fb.group({
      cc: ['', [Validators.required]],
      typeOptions: ['0', [Validators.required]],
    })
  }



  ngOnInit(): void {
    /* this.procesoService.getProcesos("get_procesos","0","0968599020001")
    .subscribe((res: any) => {
      this.data = res
      console.log(res);

    }, (err) => {
      console.log(err);
    }) */
  }


  onSubmit(){
    console.log("netra");
    if (this.dataSearchForm.valid) {
      this.procesoService.getProcesos(
        "get_procesos",
        this.dataSearchForm.get("typeOptions")!.value,
        this.dataSearchForm.get("cc")!.value
      ).subscribe((res: any) => {
        this.data = res;
      }, (err) => {
        Swal.fire({
          icon: "error",
          title: "Error",
          text: err.error.msg
        });
      })
    }

  }


}
