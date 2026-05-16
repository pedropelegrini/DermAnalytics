function cadastrar(event) {
    event.preventDefault();

    const idade = document.getElementById("idade").value;
    const sexo = document.getElementById("sexo").value;
    const tipoLesao = document.getElementById("lesao").value.trim();
    const regiao = document.getElementById("regiao").value.trim();
    const data = document.getElementById("data").value;

    if (!idade || !sexo || !tipoLesao || !regiao || !data) {
        alert("Preencha todos os campos antes de cadastrar.");
        return;
    }

    fetch("http://127.0.0.1:5000/cadastrar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            idade: idade,
            sexo: sexo,
            tipo_lesao: tipoLesao,
            regiao: regiao,
            data: data
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.mensagem);
        document.querySelector("form").reset();
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Erro ao cadastrar os dados.");
    });
}