using System;

namespace M_Test
{

    abstract class Bicho
    {

        //--------Atributos-------[

        protected string nome;
        protected int idade;
        protected string sexo;
        protected int saude;
        protected int fome;
        protected int sede;

        //------------------------]

        //-----Metodos GetSet-----[

        public string Nome
        {
            set { nome = value; }
            get { return nome; }
        }
        public int Idade
        {
            get { return idade; }
        }
        public string Sexo
        {
            get { return sexo; }
        }
        public int Saude
        {
            get { return saude; }
        }
        public int Fome
        {
            get { return fome; }
        }
        public int Sede
        {
            get { return sede; }
        }

        //-----------------------]

        //------------Metodos-------------[

        protected void envelhece()//  <-- Envelhece: Metodo responsavio por aumenta a idade
        {
            idade++;
        }
        //morte(){}

        Random rand = new Random();

        protected void newIdade(int IDmin, int IDmax)//  <-- newIdade: Metodo responsavio por gera uma idade
        {
           idade = rand.Next(IDmin, IDmax+1);
        }

        protected void newSexo(string[] sexos)//  <-- newIdade: Metodo responsavio por defini um sexo
        {
            sexo = sexos[rand.Next(0, sexos.Length)];
        }

        abstract public void info();

        //------------------------------]

        //-----Construtor-----[

        protected Bicho()
        {
            nome = "Bicho";
            saude = 100;
            fome = 50;
            sede = 50;
        }

        //--------------------]
    }


 //  -------Felino-------

    class Felino:Bicho
    {
        public Felino()
        {
            string[] sexos = new string[2]{"Macho","Fêmea"};
            newIdade(1,8);
            newSexo(sexos);
        }

        override public void info()
        {
            Console.Clear();
            Console.WriteLine("Nome: {0}\nIdade: {1}\nSexo: {2}",Nome,Idade,Sexo);
            Console.WriteLine("------------");
            Console.Write("Saude:");
            for(int i = 0; i < Saude; i+=5)
            {
                Console.Write("|");
            }
            Console.WriteLine(" - {0}%",Saude);
        }
    }

 //  -------Leporidade-------

    class Leporidae : Bicho
    {
        public Leporidae()
        {
            string[] sexos = new string[2]{"Macho","Fêmea"};
            newIdade(1,2);
            newSexo(sexos);
        }

        override public void info()
        {
            Console.Clear();
            Console.WriteLine("Nome: {0}\nIdade: {1}\nSexo: {2}",Nome,Idade,Sexo);
            Console.WriteLine("------------");
            Console.Write("Saude:");
            for(int i = 0; i < Saude; i+=5)
            {
                Console.Write("|");
            }
            Console.WriteLine(" - {0}%",Saude);
        }
    }


 //  -----------------Main-----------------------

    class main
    {
        static void Main(string[] args)
        {
            //test
            /*
            Felino gatinha = new Felino();
            gatinha.Nome = "Gatinha";
            Console.WriteLine("nome: {0}, idade: {1} sexo: {2}",gatinha.Nome,gatinha.Idade,gatinha.Sexo);
            Console.WriteLine("Saude: {0}%\nFome: {1}%  Sede: {2}%",gatinha.Saude,gatinha.Fome,gatinha.Sede);

            Leporidae coelha = new Leporidae();
            coelha.Nome = "Coelho";
            Console.WriteLine("nome: {0}, idade: {1} sexo: {2}",coelha.Nome,coelha.Idade,coelha.Sexo);
            Console.WriteLine("Saude: {0}%\nFome: {1}%  Sede: {2}%",coelha.Saude,coelha.Fome,coelha.Sede);

            */

            //==== init basic test ====
            int escolha = 0;
            string[] bichos = new string[3]{"Gato","Coelho","Slime"};

            Console.WriteLine("Escolha um bichinho para adota");

            bool loop = true;
            do
            {
              
                for (int i=0; i<bichos.Length; i++)
                {
                    Console.WriteLine("{0}-{1}", i+1, bichos[i]);
                }
                Console.Write(">>");
                escolha = int.Parse(Console.ReadLine());
                switch(escolha)
                {
                    case 1:
                        Felino gato = new Felino();
                        Console.Write("Nome: ");
                        gato.Nome = Console.ReadLine();
                        gato.info();
                        loop = false;
                        break;
                    case 2:
                        Leporidae coelho = new Leporidae();
                        Console.Write("Nome: ");
                        coelho.Nome = Console.ReadLine();
                        coelho.info();
                        loop = false;
                        break;
                    case 3:
                        loop = false;
                        break;
                    default:
                        Console.Clear();
                        Console.WriteLine("Opção invalida! escolha uma das opções a baixo.");
                        break;
                }

            }while(loop);
        }
    }

}