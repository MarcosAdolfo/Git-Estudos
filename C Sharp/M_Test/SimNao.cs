using System; 

namespace M_test
{

    class SimNao
    {
        static void Main()
        {
            String txt,bor,res;
            txt = "  Bem Vindo!";
            bor = "-=-=-=-=-=-=-=-";
            Console.WriteLine("{0}\n{1}\n{2}",bor,txt,bor);

            Escolha: // GOTO INICIO
            Console.Write("Gosto? Sim ou Nao - S/N: ");
            res = Console.ReadLine();

            switch(res)
            {
                case "Sim":
                case "sim":
                case "S":
                case "s":
                    Console.WriteLine("Que Bom Que Gosto!!!");
                    break;
                case "Não":
                case "não":
                case "Nao":
                case "nao":
                case "N":
                case "n":
                    Console.WriteLine("Faremos Melhor Na Procima Vez");
                    break;
                default:
                    Console.WriteLine("Escolha uma opção valida!!!");
                    goto Escolha;   // GOTO 01
                    break;
            }
        }
    }

}