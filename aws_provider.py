import boto3

class AwsProvider():
    def __init__(self) -> None:
        self.s3 = boto3.resource('s3')

    def upload_s3(self, path):
        data = open(path, 'rb')
        nome = data.name[data.name.rindex('/')+1:len(data.name)]

        try:
            bucket_names = self.s3.buckets.all()
            print('Lista de buckets:')
            for bucket in bucket_names:
                print('\t'+bucket.name)
        except:
            print('Por favor, verifique suas credenciais no diretório "~/.aws/credentials" e tente novamente!')
            return

        opt = input('\nPor favor, escreva o nome do bucket a seguir: ')

        self.s3.Bucket(opt).put_object(
            Key=nome, Body=data)
        print('Upload realizado no bucket S3 com sucesso')