createTableBody();

function createTableBody() {
  let rows = 50;
  let cells = 3;

  let c = 1
  
  let table = document.getElementById('task-table'); 
  let string_table = "<tr align=\"center\"><th>Место</th><th>Пользователь</th><th>Очки</th></tr>"
  for (let i=0; i < rows; i++) {
    string_table += "<tr align=\"center\">"
    string_table += `<td>${i + 1}</td>`
    for (let j=0; j < cells - 1; j++) {
        string_table += "<td></td>"}

    string_table += "</tr>"
}
table.innerHTML = string_table
};
