from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_simple_team_mappings_locale import GetSeasonSimpleTeamMappingsLocale
from ...models.get_season_simple_team_mappings_response_200 import GetSeasonSimpleTeamMappingsResponse200
from ...types import Response


def _get_kwargs(
    locale: GetSeasonSimpleTeamMappingsLocale,
    urn_season: str,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/seasons/{urn_season}/simple_team_mappings" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSeasonSimpleTeamMappingsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSeasonSimpleTeamMappingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSeasonSimpleTeamMappingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSeasonSimpleTeamMappingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonSimpleTeamMappingsResponse200]:
    """get a list of simple team mappings in a season

     Get a list of simple team mappings in a season

    Args:
        locale (GetSeasonSimpleTeamMappingsLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonSimpleTeamMappingsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSeasonSimpleTeamMappingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSeasonSimpleTeamMappingsResponse200]:
    """get a list of simple team mappings in a season

     Get a list of simple team mappings in a season

    Args:
        locale (GetSeasonSimpleTeamMappingsLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonSimpleTeamMappingsResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_season=urn_season,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetSeasonSimpleTeamMappingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonSimpleTeamMappingsResponse200]:
    """get a list of simple team mappings in a season

     Get a list of simple team mappings in a season

    Args:
        locale (GetSeasonSimpleTeamMappingsLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonSimpleTeamMappingsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSeasonSimpleTeamMappingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSeasonSimpleTeamMappingsResponse200]:
    """get a list of simple team mappings in a season

     Get a list of simple team mappings in a season

    Args:
        locale (GetSeasonSimpleTeamMappingsLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonSimpleTeamMappingsResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_season=urn_season,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
