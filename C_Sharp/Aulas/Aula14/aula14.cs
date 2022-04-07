using System; 

namespace Aula12
{

    class aula12
    {
        static void Main()
        {
            //SE(E_L){}
            //10 < 5 = false
            // < > <= >= ==
            int n1,n2,n3,n4,res;
            n1=n2=n3=n4=res=0;

            string resutado;

            Console.Write("Digite a Nota 1: ");
            n1 = int.Parse(Console.ReadLine());

            Console.Write("Digite a Nota 2: ");
            n2 = int.Parse(Console.ReadLine());

            Console.Write("Digite a Nota 3: ");
            n3 = int.Parse(Console.ReadLine());

            Console.Write("Digite a Nota 4: ");
            n4 = int.Parse(Console.ReadLine());

            res = n1+n2+n3+n4;

            if(res >= 60)
            {
                if(res >= 90)
                {
                   resutado = "Aprovado com louvor"; 
                }else{resutado = "Aprovado";}
                
            }
            else
            {
                if(res >= 40)
                {
                    resutado = "Recuperação";
                }
                else{resutado = "Reprovado";}
                
            }

            Console.WriteLine("{0}! Nota: {1}",resutado,res);
        }
    }

}