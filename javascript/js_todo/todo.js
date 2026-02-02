const taskEle = document.getElementById('taskEle');
const taskForm = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
const openBtn = document.getElementById('openBtn');


function submitTask(e){
    e.preventDefault();
    const taskValue = taskEle.value;
    
    if (taskValue == ''){
        return
    };
    
    const li = document.createElement('li');
    const span = document.createElement('span');
    const input = document.createElement('input');
    input.type = 'checkbox';

    input.addEventListener('change', function(){
        counter();
    });

    const editbtn = document.createElement('button');
    editbtn.textContent = '編集';
    editbtn.addEventListener('click', function(){
        const newText = prompt('タスクを編集してください', span.textContent);
        if (newText != '' && newText != null){
            span.textContent = newText;
            counter();
        }
    });

    const deletebtn = document.createElement('button');
    deletebtn.textContent = '削除';
    deletebtn.addEventListener('click', function(){
        if (confirm('本当に削除しますか？')) {
            li.remove();
            counter();
        }
    });

    span.textContent = taskValue;
    taskList.appendChild(li);
    counter();
    
    li.appendChild(input);
    li.appendChild(span);
    li.appendChild(editbtn);
    li.appendChild(deletebtn);
    taskEle.value = ''
}

function counter(){
    const all = document.querySelectorAll('#taskList li').length;
    const done = document.querySelectorAll('#taskList input[type="checkbox"]:checked').length;
    const todo = all - done;

    document.getElementById('allNumer').textContent = all;
    document.getElementById('doneNumer').textContent = done;
    document.getElementById('taskNumer').textContent = todo;
}

function toggleForm(e){
    e.preventDefault();
    taskForm.classList.toggle('hidden');
}

openBtn.addEventListener('click', toggleForm);
taskForm.addEventListener('submit',submitTask);