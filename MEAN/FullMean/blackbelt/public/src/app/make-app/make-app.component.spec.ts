import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MakeAppComponent } from './make-app.component';

describe('MakeAppComponent', () => {
  let component: MakeAppComponent;
  let fixture: ComponentFixture<MakeAppComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MakeAppComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MakeAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
