using System;

namespace POO_CV
{

    class banco
    {
        static void Main()
        {
            ContaBanco banco = new ContaBanco();
            banco.setNumConta(1111);
            banco.setdono("Alfredo de moras");
            banco.abrirConta("CC");
            banco.depositar(230);
            banco.sacar(50);

            Console.WriteLine("Nc: {0}\nTp: {1}\nDn: {2}\nSl: {3}\nSt: {4}",banco.getNumConta(),banco.gettipo(),banco.getdono(),banco.getsaldo(),banco.getstatus());
        }
    }

    public class ContaBanco
    {
        //--------Atributos----------

        public int numConta;
        protected string tipo;
        private string dono;
        private double saldo;
        private bool status;

        //--------Metodos Especiais-------

        public ContaBanco()
        {
            saldo = 0;
            status = false;
        }
                //SetGet numConta
        public void setNumConta(int num)
        {
            numConta = num;
        }
        public int getNumConta()
        {
            return numConta;
        }
                //SetGet tipo
        public void settipo(string t)
        {
            tipo = t;
        }
        public string gettipo()
        {
            return tipo;
        }
                //SetGet dono
        public void setdono(string d)
        {
            dono = d;
        }
        public string getdono()
        {
            return dono;
        }
                //SetGet saldo
        public void setsaldo(double s)
        {
            saldo = s;
        }
        public double getsaldo()
        {
            return saldo;
        }
                //SetGet status
        public void setstatus(bool st)
        {
            status = st;
        }
        public bool getstatus()
        {
            return status;
        }

        //--------Metodos--------

        public void abrirConta(string t)
        {
            settipo(t);
            setstatus(true);
            if(t == "cc" || t == "CC")
            {
                saldo = 50;
            }
            else if(t == "cp" || t == "CP")
            {
                saldo = 150;
            }
        }
        public void fecharConta()
        {
            if(saldo > 0)
            {
                Console.WriteLine("Conta com Dinheiro!");
            }
            else if(saldo < 0)
            {
                Console.WriteLine("Conta em débito");
            }
            else{setstatus(false);}

        }
        public void depositar(double v)
        {
            if(status)
            {
                setsaldo(getsaldo()+v);
            }
            else
            {
                Console.WriteLine("Impossivel depositar!");
            }
        }
        public void sacar(double v)
        {
            if(status = true && saldo >= v)
            {
                setsaldo(getsaldo()-v);
            }
            else
            {
                Console.WriteLine("Impossivel Saca!");
            }
        }
        public void pagarMensal()
        {
            double v=0;
            if(gettipo() == "CC" || tipo == "cc")
            {
                v = 12;
            }
            else if(tipo == "CP" || tipo == "cp")
            {
                v = 20;
            }
            if(status = true && saldo > v)
            {
                setsaldo(getsaldo()-v);
            }
            else{Console.WriteLine("Impossivel pagar!!!");}
        }
               
    }

}