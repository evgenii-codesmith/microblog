import boto3


def translate(text, source_lang, target_lang):
    translate = boto3.client(service_name='translate', use_ssl=True)
    try:
        result = translate.translate_text(
            Text=text, SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang)
        return result.get('TranslatedText')
    except Exception as e:
        return ('error')
