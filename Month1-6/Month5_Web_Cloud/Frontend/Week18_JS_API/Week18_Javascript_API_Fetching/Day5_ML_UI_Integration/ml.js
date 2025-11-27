const input = document.querySelector("#todo-input");
const addBtn = document.querySelector("#add-btn");
const list = document.querySelector("#todo-list");

addBtn.addEventListener("click", () => {
  const value = input.value.trim();

  if (value === "") return;

  const li = document.createElement("li");
  li.classList.add("todo-item");
  li.innerText = value;

  const del = document.createElement("button");
  del.innerText = "Delete";
  del.classList.add("delete-btn");

  del.addEventListener("click", () => {
    li.remove();
  });

  li.appendChild(del);
  list.appendChild(li);

  input.value = "";
});
