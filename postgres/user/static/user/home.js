const title = document.getElementById("title");
const description = document.getElementById("description");
const start_date = document.getElementById("start_date");
const end_date = document.getElementById("end_date");
const save = document.getElementById("save");

boolval = false;

const update_todo = (event) => {
  title.contentEditable = true;
  description.contentEditable = true;
  start_date.contentEditable = true;
  end_date.contentEditable = true;
  save.style = "display: block;";
};

save.addEventListener("click", (e) => {

  const csrftoken = document.cookie.split(";")[1].substring(11);
  const options = {
    method: "POST",
    headers: {
      'Accept': "application/json",
      "X-Requested-With": "XMLHttpRequest", //Necessary to work with request.is_ajax()
      "content-type": "application/json",
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    credentials: 'same-origin',
    data: JSON.stringify({
      'title': title.textContent,
      'description': description.textContent,
      'start_date': start_date.textContent,
      'end_date': end_date.textContent,
    }),
  };

  fetch("http://localhost:8000/api/v1/create/", options);

  title.contentEditable = false;
  description.contentEditable = false;
  start_date.contentEditable = false;
  end_date.contentEditable = false;
  save.style = "display: none;";
});
