


function CreateCategory(){

    let title = document.getElementById('inputText').value ;
    let file = document.getElementById('InputFile') ;

    console.log(title);
    console.log(file.files[0]);

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"


    let form_data = new FormData();
    form_data.append('title',title)
    form_data.append('file',file.files[0])



    axios.post('/CategoryCreate/',form_data)

      .then(function (response) {
        alert("Категория успешно создана")
      })
      .catch(function (error) {
        console.log(error);
      });


}




function CreateProduct(){

    let title = document.getElementById('inputText').value ;
    let image = document.getElementById('InputFile');
    let price = document.getElementById("InputNumber").value;
    let price_valuta = document.getElementById("InputValuta").value;
    let CategoryId = localStorage.getItem('CategoryId');

    const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;



    const config = {
      headers:{
        "X-CSRFTOKEN":csrftoken
      }
    };



    let form_data = new FormData();
    form_data.append('title',title)
    form_data.append('file',image.files[0])
    form_data.append('price',price)
    form_data.append('price_valuta',price_valuta)
    form_data.append('CategoryId',CategoryId)
    



    axios.post('/ProductCreate/',form_data,config)

      .then(function (response) {
        alert("Продукт успешно создан")
      })
      .catch(function (error) {
        console.log(error);
      });


}



function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}