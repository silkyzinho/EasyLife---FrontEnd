// privacy.js - controle mínimo para consentimento LGPD
(function(){
  // chave usada no localStorage
  const KEY = 'calculator_privacy_accepted_v1';

  // Marca que o usuário aceitou a política
  window.acceptPrivacy = function(){
    try {
      localStorage.setItem(KEY, 'true');
      // possível uso: fechar banner se tiver
      const banner = document.getElementById('privacy-banner');
      if(banner) banner.style.display = 'none';
    } catch(e) {
      console.warn('localStorage não disponível:', e);
    }
  };

  // Verifica se já aceitou
  window.hasAcceptedPrivacy = function(){
    try {
      return localStorage.getItem(KEY) === 'true';
    } catch(e){
      return false;
    }
  };

  // Valida formulário (passar id do form e o nome do checkbox de aceite)
  // Exemplo de uso: onsubmit="return requirePrivacyAcceptance('signup-form','privacy_accept')"
  window.requirePrivacyAcceptance = function(formId, checkboxName){
    var form = document.getElementById(formId);
    if(!form) return true; // nada a fazer se form não existe

    var checkbox = form.elements[checkboxName];
    if(!checkbox) return true;

    if(checkbox.checked) {
      // opcional: marcar consentimento global
      acceptPrivacy();
      return true;
    } else {
      alert('Você precisa aceitar a Política de Privacidade para continuar.');
      checkbox.focus();
      return false;
    }
  };

  // Se quiser mostrar um banner automaticamente:
  window.showPrivacyBannerIfNeeded = function(){
    if(!hasAcceptedPrivacy()){
      const banner = document.getElementById('privacy-banner');
      if(banner) banner.style.display = 'flex';
    }
  };

  // autopruning: tentar mostrar banner se existir na página
  document.addEventListener('DOMContentLoaded', function(){
    try { showPrivacyBannerIfNeeded(); } catch(e) {}
  });

})();
