import discord

__MESSAGES__ = {
    
"__INIT__": """
님 환영합니다!
공지사항을 확인해주세요!
봇 명령어 리스트: !help
""",

"helpEmbed":    discord.Embed(title = '도움말',        color = 0xFFBBC6),
"connectEmbed": discord.Embed(title = '접속방법',      color = 0xFFBBC6),
"cautionEmbed": discord.Embed(title = '주의사항',      color = 0xFFBBC6),
"siteEmbed":    discord.Embed(title = '유용한 사이트', color = 0xFFBBC6),

}

__MESSAGES__["helpEmbed"].add_field(name='!help',       value='봇 명령어 목록')
__MESSAGES__["helpEmbed"].add_field(name='!connect',    value='접속 방법')
__MESSAGES__["helpEmbed"].add_field(name='!caution',    value='주의 사항')
__MESSAGES__["helpEmbed"].add_field(name='!site',       value='유용한 사이트')
__MESSAGES__["helpEmbed"].add_field(name='다른 기능들', value='추후 업데이트 예정입니다')

__MESSAGES__["connectEmbed"].add_field(inline=False, name='1.', value='얼리엑세스를 실행한다.')
__MESSAGES__["connectEmbed"].add_field(inline=False, name='2.', value='메인 메뉴에서 Ctrl + Shift + L 을 누른다.')
__MESSAGES__["connectEmbed"].add_field(inline=False, name='3.', value='이후 ~ 을 누른다.')
__MESSAGES__["connectEmbed"].add_field(inline=False, name='4.', value="게임 하단에 콘솔창이 표시되면 'open gorae.kro.kr' 을 입력한다.")

__MESSAGES__["cautionEmbed"].add_field(inline=False, name='1.',   value='게임을 종료할때 혹시 모르니 인벤에 있는 모든 물품은 창고에 보관하고 종료하기를 바랍니다.')
__MESSAGES__["cautionEmbed"].add_field(inline=False, name='2.',   value='전적으로 5분 자동 저장에 의존하고 있기 때문에 서버가 갑자기 닫히면 정보가 날아갈 수 있습니다.')
__MESSAGES__["cautionEmbed"].add_field(inline=False, name='3.',   value='접속할때 충돌 오류가 나는 경우가 있습니다. 그럴땐 침착하게 접속 재시도 부탁드립니다.')
__MESSAGES__["cautionEmbed"].add_field(inline=False, name='3-1.', value='위 현상이 반복될 시 <@!319394108387098625>를 불러주세요')
__MESSAGES__["cautionEmbed"].add_field(inline=False, name='4.',   value="멀티플레이 버그로 인해 나무 등 오브젝트가 복구되는 버그가 있으니 양해 부탁드립니다.")

__MESSAGES__["siteEmbed"].add_field(inline=False, name='공식사이트',    value=r'https://www.satisfactorygame.com/')
__MESSAGES__["siteEmbed"].add_field(inline=False, name='공식위키',      value=r'https://satisfactory.fandom.com/wiki/Satisfactory_Wiki')
__MESSAGES__["siteEmbed"].add_field(inline=False, name='상호작용 지도', value=r'https://satisfactory-calculator.com/ko/interactive-map')
__MESSAGES__["siteEmbed"].add_field(inline=False, name='3d 지도',       value=r'https://ficsit-felix.netlify.app/#/%2F')
__MESSAGES__["siteEmbed"].add_field(inline=False, name='계산기',        value=r'https://www.satisfactorytools.com/production')
__MESSAGES__["siteEmbed"].add_field(inline=False, name='그래프토리',    value=r'https://satisgraphtory.com/')
__MESSAGES__["siteEmbed"].add_field(inline=False, name='트위터',        value=r'https://twitter.com/satisfactoryaf/')
