function botao_excluir(){
    alert("Excluiu tudo")
}
function botao_investir(){
    alert("Investiu Tudo")
}
function botao_user(){
    
}
function somatorio_valor_acoes(input){
    var total = 0;
    for(var i=0 ;i<input.lenght;i++){
        total = input[i] + total;
    }
    return total
}