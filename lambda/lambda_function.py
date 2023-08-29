# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import text
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_inicial

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                .response
        )

#-ATIVO-#
class AtivoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtivoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_ativo

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-PASSIVO-#
class PassivoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PassivoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_passivo

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-VALOR CONTÁBIL-#
class ValorContabilIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ValorContabilIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_valor_contabil

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-RECURSO ECONÔMICO-#
class RecursoEconomicoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RecursoEconomicolIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_recursos_economicos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-PATRIMÔNIO LIQUIDO-#
class PatrimonioLiquidoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PatrimonioLiquidolIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_patrimonio_liquido

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-RECEITA-#
class ReceitaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ReceitalIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_receita

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-DESPESA-#
class DespesaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DespesalIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_despesa

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-VALOR REALIZÁVEL LÍQUIDO-#
class ValorRealizavelLiquidoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ValorRealizavelLiquidoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_valor_realizavel_liquido

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-ESTOQUE-#
class EstoqueIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EstoqueIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_estoque

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
#                                  #                                        #
#-VALOR JUSTO-#
class ValorjustoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ValorJustoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_valor_justo

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-CUSTO-#
class CustoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_custo

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-DEPRECIAÇÃO-#
class DepreciacaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DepreciacaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_depreciacao

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-DINHEIRO-#
class DinheiroIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DinheiroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_dinheiro

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-CAIXA-#
class CaixaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaixaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_caixa

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-EQUIVALENTES DE CAIXA-#
class EquivalentesDeCaixaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EquivalentesDeCaixaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_equivalentes_de_caixa

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-FLUXO DE CAIXA-#
class FluxoDeCaixaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FluxoDeCaixaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_fluxo_de_caixa

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-ATIVIDADES OPERACIONAIS-#
class AtividadesOperacionaisIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtividadesOperacionaisIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_atividades_operacionais

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-ATIVIDADES DE INVESTIMENTO-#
class AtividadesDeInvestimentoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtividadesDeInvestimentoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_atividades_de_investimento

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-ATIVIDADES DE FINANCIAMENTO-#
class AtividadesDeFinanciamentoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtividadesDeFinanciamentoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_atividades_de_financiamento

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-ARRENDAMENTO-#
class ArrendamentoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ArrendamentoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_arrendamento

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-SUBARRENDAMENTO-#
class SubarrendamentoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SubarrendamentoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_subarrendamento

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-VIDA UTIL-#
class VidaUtilIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VidaUtilIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_vida_util

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-DEPRECIAÇÃO 2 -#
class AmortizacaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AmortizacaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_depreciacao2

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-VALOR ADICIONADO -#
class ValorAdicionadoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ValorAdicionadoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_valor_adicionado

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-OUTRAS RECEITAS -#
class OutrasReceitasIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OutrasReceitasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_outras_receitas

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- ATIVO BIOLÓGICO -#
class AtivoBiologicoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtivoBiologicoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_ativo_biologico

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- ATIVIDADE AGRÍCOLA -#
class AtividadeAgricolaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtividadeAgricolaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_atividade_agricola

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- PRODUÇÃO AGRÍCOLA -#
class ProducaoAgricolaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ProducaoAgricolaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_producao_agricola

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- RESULTADO CONTÁBIL -#
class ResultadoContabilIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ResultadoContabilIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_resultado_contabil

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- RESULTADO TRIBUTÁVEL -#
class ResultadoTributavelIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ResultadoTributavelIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_resultado_tributavel

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- BENEFICIOS A EMPREGADOS-#
class BenenficiosaEmpregadosIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BenenficiosaEmpregadosIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_beneficios_a_empregados

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- ATIVO FINANCEIRO-#
class AtivoFinanceiroIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AtivoFinanceiroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_ativo_financeiro

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#- PASSIVO FINANCEIRO-#
class PassivoFinanceiroIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PassivoFinanceiroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = text.msg_passivo_financeiro

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
#======================================================================================================#
class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "OPA, Algo deu errado, Você pode pedir ajuda?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Tchau!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, Não tenho certeza. Você pode falar Ola ou Ajuda.Como gostaria de fazer?"
        reprompt = "Não consegui enteder essa. Como posso te ajudar com isso?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Desculpa, Estou tendo problemas com o que você me pediu. Tente novamente."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AtivoIntentHandler())
sb.add_request_handler(PassivoIntentHandler())
sb.add_request_handler(ValorContabilIntentHandler())
sb.add_request_handler(RecursoEconomicoIntentHandler())
sb.add_request_handler(PatrimonioLiquidoIntentHandler())
sb.add_request_handler(ReceitaIntentHandler())
sb.add_request_handler(DespesaIntentHandler())
sb.add_request_handler(ValorRealizavelLiquidoIntentHandler())
sb.add_request_handler(EstoqueIntentHandler())
sb.add_request_handler(ValorjustoIntentHandler())
sb.add_request_handler(CustoIntentHandler())
sb.add_request_handler(DepreciacaoIntentHandler())
sb.add_request_handler(DinheiroIntentHandler())
sb.add_request_handler(CaixaIntentHandler())
sb.add_request_handler(EquivalentesDeCaixaIntentHandler())
sb.add_request_handler(FluxoDeCaixaIntentHandler())
sb.add_request_handler(AtividadesOperacionaisIntentHandler())
sb.add_request_handler(AtividadesDeInvestimentoIntentHandler())
sb.add_request_handler(AtividadesDeFinanciamentoIntentHandler())
sb.add_request_handler(ArrendamentoIntentHandler())
sb.add_request_handler(SubarrendamentoIntentHandler())
sb.add_request_handler(VidaUtilIntentHandler())
sb.add_request_handler(AmortizacaoIntentHandler())
sb.add_request_handler(ValorAdicionadoIntentHandler())
sb.add_request_handler(OutrasReceitasIntentHandler())
sb.add_request_handler(AtivoBiologicoIntentHandler())
sb.add_request_handler(AtividadeAgricolaIntentHandler())
sb.add_request_handler(ProducaoAgricolaIntentHandler())
sb.add_request_handler(ResultadoContabilIntentHandler())
sb.add_request_handler(ResultadoTributavelIntentHandler())
sb.add_request_handler(BenenficiosaEmpregadosIntentHandler())
sb.add_request_handler(AtivoFinanceiroIntentHandler())
sb.add_request_handler(PassivoFinanceiroIntentHandler())
##
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()