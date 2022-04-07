using System;
using System.Globalization;

class URI
{
    static void Main(string[] args)
    { 
        string nome;
        double salario,totVendas,total;
        
        nome = Console.ReadLine();
        salario = double.Parse(Console.ReadLine());
        totVendas = double.Parse(Console.ReadLine());
        total = salario + ((totVendas*15)/100);
        
        Console.WriteLine("TOTAL = R$ {0}",total.ToString("F2",CultureInfo.InvariantCulture));

        //################################

        /*
        int num,horasDeTrabalho;
        double vHoras,salario;
        
        num = int.Parse(Console.ReadLine());
        horasDeTrabalho = int.Parse(Console.ReadLine());
        vHoras = double.Parse(Console.ReadLine());
        
        salario = horasDeTrabalho*vHoras;

        Console.WriteLine("NUMBER = {0} SALARY = U$ {1}",num,salario.ToString("F2",CultureInfo.InvariantCulture));*/
        

        //################################

        /*
        int A,B,C,D,DIFERENCA;
        
        A = int.Parse(Console.ReadLine());
        B = int.Parse(Console.ReadLine());
        C = int.Parse(Console.ReadLine());
        D = int.Parse(Console.ReadLine());
        
        DIFERENCA = ((A*B)-(C*D));
        
        Console.WriteLine("DIFERENCA = {0}",DIFERENCA);*/

        //################################

        /*
        double A,B,C,MEDIA;
        
        A = double.Parse(Console.ReadLine());
        B = double.Parse(Console.ReadLine());
        C = double.Parse(Console.ReadLine());
        
        MEDIA = ((A*2)+(B*3)+(C*5))/(2+3+5);
        
        Console.WriteLine("MEDIA = {0}",MEDIA.ToString("F1",CultureInfo.InvariantCulture));*/

        //##############################

        /*
        int x,y,PROD;
        
        x = int.Parse(Console.ReadLine());
        y = int.Parse(Console.ReadLine());
        
        PROD = x * y;
        
        Console.WriteLine("PROD = {0}",PROD);*/

        //################################

        /*
        int SOMA,A,B;
        
        A = int.Parse(Console.ReadLine());
        B = int.Parse(Console.ReadLine());
        
        SOMA=A+B;
        Console.WriteLine("SOMA = {0}",SOMA);*/

        //################

        /*
        double area,raio,n;

        n = 3.14159;

        raio = double.Parse(Console.ReadLine());
        area = n * (Math.Pow(raio,2));

        Console.WriteLine("A={0}",area.ToString("F4",CultureInfo.InvariantCulture));*/


        //#####################


        /*
        int A,B,X;
        
        Console.Write("Digite o primeiro numero: ");
        A = int.Parse(Console.ReadLine());
        Console.Write("Digite o segundo numero: ");
        B = int.Parse(Console.ReadLine());
        
        X = A + B;
        
        Console.WriteLine("X = {0}",X); */
        
    }

}