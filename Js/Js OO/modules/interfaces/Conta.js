export class Conta{

    constructor(agencia, cliente) {
        this.agencia = agencia;
        this.saldo = 0
        this.cliente = cliente;
    };

    sacar(valor) {
        if(this.saldo >= valor){
            this.saldo -= valor;
            return valor;
        }
    };

    depositar(valor){
        if(valor <= 0) return;
        this.saldo += valor;      
        
        console.log(`Depósito de R$ ${this.saldo} realizado`)
    };

    transferir(valor, conta) {
        if(valor > this.getSaldo()) return;

        console.log(`Valor inicial: R$ ${this.getSaldo()}`);

        const sacado = this.sacar(valor);

        conta.depositar(sacado);

        console.log(`Valor final: R$ ${this.getSaldo()}`);
        
    };

    getSaldo(){
        return this.saldo;
    };

    setAgencia(valor) {
        if(!valor) return;
        if(valor.length > 4) return;

        this.agencia = valor;
    }

    setCliente(valor){ 
        this.cliente = valor;
    };


}