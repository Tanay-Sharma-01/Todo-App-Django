const delete_todo = (e) => {
    console.log(e.target)
    console.log(e.target.name)
    pk = e.target.name

    const options = {
        method: "GET",
        headers: {
          "Authorization": "TOKEN "
        },
        body: pk,
    };

    response = fetch("http://localhost:8000/api/v1/delete-todo/" , options)

}
const update_todo = () => {
    console.log("he");
}