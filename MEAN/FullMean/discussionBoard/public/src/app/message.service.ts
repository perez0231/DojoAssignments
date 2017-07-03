import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs'

@Injectable()
export class MessageService {

  constructor(private _http: Http) { }

  create(user){
    console.log("services")
    return this._http.post('/user', user)
    .map((data) => {
      console.log(data)
      console.log("users service return")
      return data.json()
  })
    .toPromise();
  }


mkQuestion(question){
  console.log("question service")
  return this._http.post('/questions', question)
  .map((data) =>{
    console.log(data)
    return data.json()
  })
  .toPromise();
}

allQuestions(){
  console.log("getting all questions")
  return this._http.get('/questions')
  .map((data)=>{
    console.log(data)
    return data.json()
  })
  .toPromise()
}




success(){
    return this._http.get('/success')
    .map(data => data.json())
    .toPromise();
  }

show(id){
  return this._http.get(`/questions/${id}`)
  .map((data)=> {
    return data.json()
  })
  .toPromise()
}

createAnswer(id, answer){
  return this._http.post(`/answers/${id}`, answer)
  .map((data)=> {
    return data.json()
  })
  .toPromise()
}


login(user){
return this._http.post('/login', user)
.map((data)=>{
  return data.json()
})
.toPromise()
}
likeanswer(id){
  return this._http.post(`/answers/${id}/like`, {id:id})
  .map((data)=>{
    return data.json()
  })
  .toPromise()
}



}
