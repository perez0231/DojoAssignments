//modules
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

//components
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductCreationComponent } from './product-creation/product-creation.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', component: HomeComponent},
  { path: 'products/list',  component: ProductListComponent},
  { path: 'products/create', component: ProductCreationComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
